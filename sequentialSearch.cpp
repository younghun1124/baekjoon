#include <iostream>
#include <stdio.h>
#include <time.h>
#include <fstream>
#include <string>
int main(void){
    clock_t start,stop=0;   // 코드 동작 시간 계산 위해 선언
    double result=0;    // 코드 동작 시간 계산 위해 선언
    std::ifstream file("C:/numbers_0_to_10000000.txt");  // 파일을 열기
    if (!file.is_open()) {
        std::cerr << "파일을 열 수 없습니다." << std::endl;
        return 1;
    } 
    std::string N;
    std::cin>>N; //찾을 수 N 입력받기
    start=clock();  // 코드 시작시간

//실행할 코드 삽입
int i=0;//탐색중인 인덱스 번호
    std::string line;
    while (std::getline(file, line)) {  // 파일에서 한 줄씩 읽기
        if (line == N) {  // 읽은 줄이 N과 같은지 비교
            std::cout<<i<<"번째 인덱스에서 발견"<<'\n';//몇번째에 발견했는지 값 리턴
            break;
        }
        i++;//탐색 인덱스 증가
    }
//
    stop=clock(); //코드 종료시간
result =(double)(stop-start)/CLOCKS_PER_SEC; //코드 수행에 소요된 시간 계산
printf("걸린 시간은 %f초 입니다.", result); //코드 수행에 소요된 시간 출력

return 0;// 프로그램 종료
}

