#include <stdio.h>
#include <time.h>

int main(void){
    clock_t start,stop=0;   // 코드 동작 시간 계산 위해 선언
    double result=0;    // 코드 동작 시간 계산 위해 선언
    start=clock();  // 코드 시작시간
    FILE* fp= fopen("APSOLUTE_PATH\\1.in","r"); //주어진 파일 읽어옴
    if(fp==NULL)return -1; // 파일 읽지 못했을 때 프로그램 종료

//실행할 코드 삽입
  for (int i=0; i<10000001; i++)
        int temp;
        fscanf(fp,"%d", &temp);
//
    stop=clock(); //코드 종료시간
result =(double)stop-start/CLOCKS_PER_SEC; //코드 수행에 소요된 시간 계산
printf("걸린 시간은 %f초 입니다.", result); //코드 수행에 소요된 시간 출력

return 0;// 프로그램 종료
}

