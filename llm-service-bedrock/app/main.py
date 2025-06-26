from services.bedrock_client import invoke_bedrock_model

prompt = '{"inputText": "안녕, 오늘 날씨 어때?"}'  # 실제 모델에 맞는 JSON 포맷 필요
model_id = "amazon.titan-text-lite-v1"  # 예시 모델 ID

result = invoke_bedrock_model(prompt, model_id)
print(result)