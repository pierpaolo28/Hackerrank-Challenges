int cnt =0;
int i=0;
int j =0;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {

  for(j = 1; j < n+1; j++)
{
    int a=0,count=0;
    for(int i=0;i<s.length();i++)
    {
        if(s[i]=='U')
            a++;
        else
            a--;
        if(a==0 && s[i]=='U')
            count++;
    }
    return count;
}

printf("%d", cnt);

return 0;
}
