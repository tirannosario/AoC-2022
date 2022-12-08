#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 1024

int findMinIndex(int* podium) {
    
    int minIndex = 0;
    int min = podium[minIndex];

    for(int i=1; i<3; i++){
        if(podium[i] < min) {
            minIndex = i;
            min = podium[minIndex];
        }
    }
    return minIndex;
}

int main(){
    FILE* fp = fopen("input.txt", "r");
    if (fp==NULL){
        fprintf(stderr, "Open file: failed...\n");
        return 0;
    } else {
        char line[BUF_SIZE];
        int current_sum=0;
        int podium[3] = {-1,-1,-1};
        int min_index = 0;

        while(fgets(line,BUF_SIZE,fp)!=NULL){
            if(line[0]=='\n'){
                if(current_sum > podium[min_index]) {
                    podium[min_index] = current_sum;
                    min_index = findMinIndex(podium);
                }
                current_sum = 0;
            }else{
                current_sum+=atoi(line);
            }
        }
        fclose(fp);

        fprintf(stdout, "The sum of the top 3 elves calories is %d", podium[0]+podium[1]+podium[2]);
    }

    return 1;
}
 
