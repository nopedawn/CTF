#include<stdio.h>
#include<stdlib.h>

struct data {
    char *str;
};
char flag[40];
struct data *survei[8];

void printMenu() {
    printf("1. Isi survei\n2. Lihat survei\n3. Keluar\n> ");
}

void isiSurvei() {
    int p;
    printf("Di manakah survei ingin disimpan?: ");
    scanf("%d", &p);
    printf("Isi survei: ");
    scanf("%s", survei[p]->str);
    printf("Survei berhasil disimpan di: %d\n", p);
}

void lihatSurvei() {
    int p;
    printf("Survei manakah yang ingin dilihat: ");
    scanf("%d", &p);
    printf("%s\n", survei[p]->str);
}

int main(int argc, char const *argv[]) {
    setvbuf(stdout, NULL, _IONBF, 0);
    FILE *fp = fopen("flag.txt", "r");
    fgets(flag, 40, fp);
    
    int i;
    for (i = 0; i < 8; i++) {
        survei[i] = malloc(sizeof(struct data));
        survei[i]->str = malloc(32);
    }
    
    while (1) {
        printMenu();
        int choice;
        scanf("%d", &choice);
        if (choice == 1) {
            isiSurvei();
        } else if (choice == 2) {
            lihatSurvei();
        } else {
            printf("Bye.\n");
            return 0;
        }
    }
}
