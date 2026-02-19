# 추천 테스트
requirements = "게임과 영상 편집을 많이 하는데, 가성비 좋은 제품을 찾고 있어요"

recommendation = analyzer.recommend(products, requirements)

print(f"추천 상품: {recommendation.get('recommended_product')}")
print(f"추천 이유: {recommendation.get('reason')}")
print(f"적합도: {recommendation.get('match_score')}/10")
