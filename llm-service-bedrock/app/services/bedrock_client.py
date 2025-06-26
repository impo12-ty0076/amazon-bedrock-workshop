import boto3
import os


def get_bedrock_runtime_client():
    """
    Bedrock Runtime 클라이언트 생성 함수
    환경 변수에서 region, profile 등을 읽어옵니다.
    """
    region = os.getenv("AWS_REGION", "us-west-2")
    profile = os.getenv("AWS_PROFILE")

    session_kwargs = {"region_name": region}
    if profile:
        session_kwargs["profile_name"] = profile

    session = boto3.Session(**session_kwargs)
    return session.client("bedrock-runtime")


def invoke_bedrock_model(prompt: str, model_id: str):
    """
    Bedrock 모델을 호출하는 기본 함수
    """
    client = get_bedrock_runtime_client()
    response = client.invoke_model(
        modelId=model_id,
        body=prompt.encode("utf-8"),
        contentType="application/json",
        accept="application/json"
    )
    return response["body"].read().decode("utf-8") 