# 골드바흐의 추측은 2보다 큰 짝수가 주어졌을 때, 해당 수는 두개의 소수의 합으로 표현할 수 있다는 것이다.
# 이러한 과정에서 나온 두 소수를 골드바흐 파티션이라고하고, 그 n을 구하는 문제이다.
# 2보다 큰 짝수에 대응하는 더하는 수가 소수면 결과로 표현시키면 되는거 아닌가? 라고 했지만 아니었다.
# 우선적으로 소수를 판별할 수 있는 에라토스네스의 체를 함수로 구현해야한다.
def is_prime(n):   #소수 판별 함수
    if n < 2:      # 1은 소수가 아님
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        # 2부터 √n까지 반복, 시간 복잡도를 줄이기위해서 범위를 줄인 것이다.
        # 해당 부분이 나는 굉장히 헷갈리는데, 직접해보니 √n까지만 처리해도 해당 숫자까지의 검사를 마칠 수 있다.
        # 원래처럼 n을 대입해서 계산하면 계산할 필요없는 경우까지 계산한다.
        if n % i == 0:  # 나누어떨어지면 소수가 아님
            return False
    return True  # 위 조건을 모두 통과하면 소수

T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    N = int(input())  # 짝수 N 입력

    for a in range(N // 2, 1, -1):  # N의 절반부터 작은 방향으로 1씩 줄이면서 탐색
        b = N - a  # a + b = N을 만족해야 함
        if is_prime(a) and is_prime(b):  # 체를 통해 둘 다 소수인지 확인
            print(a, b)
            break  # 가장 차이가 작은 쌍을 찾으면 종료
        
# GPT의 도움을 많이 받았다. 수학을 안한지 오래되서(통신 공학수학만해서...)
# 에라토스네스의 체로 소수를 구하는 함수는 꼭 다시 써보면서 외워야겠다.
# 골드바희의 추축과 에라토스네스의 체는 이론부터 어려운 것 같다.