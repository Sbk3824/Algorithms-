int strStr(char* s, char* n) {
    int i;
    int j;
    int size;
    
    size = 0;
    i = 0;
    j = 0;
    
    while(n[size])
        size++;
    if (size == 0)
        return (0);
    while(s[i])
    {
        while (s[i+j] == n[j])
        {
            if(j == size -1)
                return (i);
            j++;
        }
        j = 0;
        i++;
    }
    return (-1);
}
