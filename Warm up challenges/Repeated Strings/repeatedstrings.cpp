// Complete the repeatedString function below.
long repeatedString(string s, long n) {
long count=0;
    int i,k=s.size();
    long p=n/k;

      for(i=0;i<s.size();i++){
        if(s[i]=='a')
            count++;
      }

    count = count * p;

    for(i=0;i<(n%s.size());i++){
        if(s[i]=='a')
            count++;
    }
    return count;
}
