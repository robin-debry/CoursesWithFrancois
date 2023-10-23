#include <stdlib.h>
#include <stdio.h>

int main(void){
    FILE *bitmap, *bitmap_out;
    int type,w,h,d;

    printf("RGB Color Test\n");
    bitmap = fopen("ada.pbm", "r");
    bitmap_out = fopen("out.pbm", "w");

    if (bitmap){
        if (bitmap_out){
            fscanf(bitmap, "P%d%d%d%d ", &type, &w, &h, &d);
            printf("type = %d, width = %d, height = %d, palette size = %d\n", type, w, h, d);

            fprintf(bitmap_out, "P%d %d %d %d ", type, w, h, d);

            // read original bitmap
            // and convert it
            {
                int pixel_index;
                uint8_t r, g, b, l;
                for(pixel_index = 0; pixel_index < w * h; pixel_index++){
                    fread(&r, sizeof(uint8_t), 1, bitmap);
                    fread(&g, sizeof(uint8_t), 1, bitmap);
                    fread(&b, sizeof(uint8_t), 1, bitmap);

                    // Do your conversion process here

                    fwrite(&r, 1, 1, bitmap_out);
                    fwrite(&r, 1, 1, bitmap_out);
                    fwrite(&r, 1, 1, bitmap_out);
                }
            }
            fclose(bitmap_out);
        }
        fclose(bitmap);
    }

    return 0;
}