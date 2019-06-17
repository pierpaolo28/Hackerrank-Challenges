// Complete the rotLeft function below.
vector<int> rotLeft(vector<int> a, int d, int n) {

  d %= n;
    vector<int> vec(n);
    for(int i = 0; i < n; i++) {
        vec[(n+i-d)%n] = a[i];
    }
    return vec;
}
