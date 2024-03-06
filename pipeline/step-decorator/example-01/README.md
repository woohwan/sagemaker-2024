- 에러 해결  
1. role 에러: SageMakerExecutionRole의 trust relationship의 AdminRole로 변경.  
2. No module import sagemaker  
   Step 수행 시 keep_alive_period_in_seconds 속성이 들어갈 경우, warm pool로 빨리 수행할 수 있을 경우, (1H 이내)  
   빈 Machine을 받는 데, 임시적으로 SageMaker용 DLC를 할당해서 해결.  
   참고: https://github.com/aws/deep-learning-containers/blob/master/available_images.md  


   config.yaml 수정  
   ImageUri: '763104351884.dkr.ecr.ap-northeast-2.amazonaws.com/pytorch-training:2.2.0-cpu-py310-ubuntu20.04-sagemaker'  

   -- watch log
   2024-03-06 13:58:54,209 sagemaker.remote_function INFO     Running command: '/opt/conda/bin/python -m pip install -r /sagemaker_remote_function_workspace/requirements.txt -U' in the dir: '/'   

   ....

   2024-03-06 13:58:54,927 sagemaker.remote_function INFO     Requirement already satisfied: sagemaker<3,>=2.199.0 in /opt/conda/lib/python3.10/site-packages (from -r /sagemaker_remote_function_workspace/requirements.txt (line 3)) (2.208.0)  