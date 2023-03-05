# 폰트
- malgunsl.ttf
- batang.ttc
- gulim.ttc
- H2GTRE.TTF
- HANBatang.ttf
- HANBatangB.ttf
- Hancom Gothic Bold.ttf
- Hancom Gothic Regular.ttf
- HANDotum.ttf
- HANDotumB.ttf
- malgun.ttf
- malgunbd.ttf

# 시행착오
1. DataGenerator 오류  
__ len __ 실수
2. 모델 오류  
input_shape 잘못 잡음
3. 과적합  
데이터를 너무 적게 만듬. 레퍼런스에서는 50만 개지만, 난 30만 개였음  
그리고 고딕체와 고딕이 같다는 것을 까먹었음
4. 사실 과적합 실수임  
__ len __ 을 또 실수 함. 279만 개의 dataset 그대로 하려 했으나 1 epoch 에 6시간 잡혀서 dataset 삭제 (30분)
5. 

# 참고
- https://github.com/junstar92/hangul-syllable-recognition
- https://junstar92.tistory.com/154
- https://github.com/IBM/tensorflow-hangul-recognition/blob/master/tools/hangul-image-generator.py

# 감사드립니다
- 좋은 자료 및 해결책이 되어주신 "별준" 님께 감사드립니다