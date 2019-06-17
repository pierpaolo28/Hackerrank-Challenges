// Complete the minimumSwaps function below.
int minimumSwaps(vector<int> arr) {
   int i,c=0,n=arr.size();
    for(i=0;i<n;i++)
    {
        if(arr[i]==(i+1))
            continue;

        swap(arr[i],arr[arr[i]-1]);
        c++;
        i--;
    }
    return c;
}
