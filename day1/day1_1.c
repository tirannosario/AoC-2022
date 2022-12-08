#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUF_SIZE 1024

int main(){
    FILE* fp = fopen("input.txt", "r");

    if (fp==NULL){
        fprintf(stderr, "Open file: failed...\n");
        return 0;
    } else {
        char line[BUF_SIZE];
        int max_sum=-1;
        int current_sum=0;

        int current_elf=0;
        int max_elf=-1;


        while(fgets(line,BUF_SIZE,fp)!=NULL){
            if(line[0]=='\n'){
                if(current_sum>max_sum){
                    max_sum=current_sum;
                    max_elf=current_elf;
                }
                current_sum=0;
                current_elf++;
            }else{
                current_sum+=atoi(line);
            }
        }
        fclose(fp);

        fprintf(stdout, "Elf n.%d with %d calories is the winner", max_elf, max_sum);
    }
    
    return 1;
}