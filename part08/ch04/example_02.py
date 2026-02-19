class ProductChatbot:
    # ... 기존 코드 ...

    def process(self, user_input: str, session_id: str = "default") -> str:
        """사용자 입력 처리 (명령어 또는 대화)"""
        user_input = user_input.strip()

        # 명령어 처리
        if user_input.startswith("/"):
            return self._handle_command(user_input)

        # 일반 대화
        return self.chat(user_input, session_id)

    def _handle_command(self, command: str) -> str:
        """명령어 처리"""
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        commands = {
            "/help": self._cmd_help,
            "/add": self._cmd_add,
            "/list": self._cmd_list,
            "/remove": self._cmd_remove,
            "/clear": self._cmd_clear,
            "/analyze": self._cmd_analyze,
            "/compare": self._cmd_compare,
            "/recommend": self._cmd_recommend,
        }

        handler = commands.get(cmd)
        if handler:
            return handler(args)
        else:
            return f"알 수 없는 명령어: {cmd}\n/help로 도움말을 확인하세요."

    def _cmd_help(self, args: str) -> str:
        """도움말"""
        return """
📌 상품 비교 챗봇 명령어

/add <URL>      - 상품 추가 (URL에서 정보 추출)
/list           - 등록된 상품 목록
/remove <번호>  - 상품 삭제
/clear          - 전체 삭제
/analyze <번호> - 상품 분석
/compare        - 전체 상품 비교
/recommend <요구사항> - 맞춤 추천
/help           - 도움말

💬 일반 질문도 가능합니다!
예: "가장 가성비 좋은 제품은?" "배터리가 오래가는 제품 추천해줘"
"""

    def _cmd_add(self, args: str) -> str:
        """상품 추가"""
        if not args:
            return "사용법: /add <URL>"

        # URL 형식 확인
        if not args.startswith("http"):
            return "올바른 URL을 입력해주세요."

        # 스크래핑
        product = self.scraper.scrape(args)

        if product:
            self.store.add(product)
            return f"✅ 상품 추가됨: {product.name} ({product.price:,}원)"
        else:
            return "❌ 상품 정보를 추출할 수 없습니다."

    def _cmd_list(self, args: str) -> str:
        """상품 목록"""
        products = self.store.get_all()
        if not products:
            return "등록된 상품이 없습니다.\n/add <URL>로 상품을 추가하세요."

        lines = ["📦 등록된 상품 목록\n"]
        for i, p in enumerate(products, 1):
            lines.append(f"{i}. {p.name}")
            lines.append(f"   💰 {p.price:,}원")
            lines.append(f"   🔗 {p.url[:50]}...")
            lines.append("")

        return "\n".join(lines)

    def _cmd_remove(self, args: str) -> str:
        """상품 삭제"""
        if not args:
            return "사용법: /remove <번호>"

        try:
            index = int(args) - 1
            products = self.store.get_all()

            if 0 <= index < len(products):
                product = products[index]
                self.store.remove(product.url)
                return f"✅ 삭제됨: {product.name}"
            else:
                return f"❌ 잘못된 번호입니다. (1-{len(products)})"
        except ValueError:
            return "번호를 입력해주세요."

    def _cmd_clear(self, args: str) -> str:
        """전체 삭제"""
        self.store.clear()
        return "✅ 모든 상품이 삭제되었습니다."

    def _cmd_analyze(self, args: str) -> str:
        """상품 분석"""
        products = self.store.get_all()
        if not products:
            return "등록된 상품이 없습니다."

        if not args:
            return "사용법: /analyze <번호>"

        try:
            index = int(args) - 1
            if 0 <= index < len(products):
                product = products[index]
                result = self.analyzer.analyze(product)

                lines = [f"📊 {product.name} 분석 결과\n"]
                lines.append(f"요약: {result.get('summary', 'N/A')}")
                lines.append(f"\n👍 장점:")
                for pro in result.get('pros', []):
                    lines.append(f"  - {pro}")
                lines.append(f"\n👎 단점:")
                for con in result.get('cons', []):
                    lines.append(f"  - {con}")
                lines.append(f"\n🎯 추천 대상: {result.get('target_user', 'N/A')}")
                lines.append(f"💰 가성비: {result.get('value_rating', 'N/A')}")

                return "\n".join(lines)
            else:
                return f"❌ 잘못된 번호입니다. (1-{len(products)})"
        except ValueError:
            return "번호를 입력해주세요."

    def _cmd_compare(self, args: str) -> str:
        """상품 비교"""
        products = self.store.get_all()
        if len(products) < 2:
            return "비교하려면 2개 이상의 상품이 필요합니다."

        result = self.analyzer.compare_text(products)
        return f"📊 상품 비교 분석\n\n{result}"

    def _cmd_recommend(self, args: str) -> str:
        """맞춤 추천"""
        products = self.store.get_all()
        if not products:
            return "등록된 상품이 없습니다."

        if not args:
            return "사용법: /recommend <요구사항>\n예: /recommend 게임용으로 가성비 좋은 것"

        result = self.analyzer.recommend(products, args)

        if "error" in result:
            return f"❌ 추천 실패: {result['error']}"

        lines = ["🎯 맞춤 추천 결과\n"]
        lines.append(f"추천 상품: {result.get('recommended_product', 'N/A')}")
        lines.append(f"추천 이유: {result.get('reason', 'N/A')}")
        lines.append(f"적합도: {result.get('match_score', 'N/A')}/10")

        return "\n".join(lines)
