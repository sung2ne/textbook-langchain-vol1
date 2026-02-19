def generate_data_summary(df: pd.DataFrame) -> str:
    """데이터프레임 요약 생성"""
    summary = []

    # 기본 정보
    summary.append(f"총 {len(df)}개 레코드, {len(df.columns)}개 컬럼")
    summary.append(f"컬럼: {', '.join(df.columns.tolist())}")

    # 숫자형 컬럼 통계
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        summary.append(f"{col}: 평균 {df[col].mean():.2f}, 최소 {df[col].min()}, 최대 {df[col].max()}")

    # 카테고리형 컬럼 통계
    object_cols = df.select_dtypes(include=['object']).columns
    for col in object_cols:
        unique_count = df[col].nunique()
        summary.append(f"{col}: {unique_count}개 고유값")

    return "\n".join(summary)


# 사용
summary = generate_data_summary(df)
print(summary)
