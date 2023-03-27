#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int left, int right) {
    int result = 0;
    for(int i=left;i<=right;i++){
        int count = 0;
        for(int j=1;j<=i;j++){
            if(i%j==0){
                count += 1;
            }
        }
        if(count%2==0){
            result += i;
        }
        else{
            result -= i;
        }
    }
    return result;
}