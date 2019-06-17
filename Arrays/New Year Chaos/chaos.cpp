// Complete the minimumBribes function below.
void minimumBribes(vector<int> q) {
  // if vector is ascending ardered everything ok
  // if is not but each number is out of place by max 2 order it and count
  // if is not ordered and at least one number is out of place of more than 2, system caothic
    int ans = 0;
    for (int i = q.size() - 1; i >= 0; i--) {
        if (q[i] - (i + 1) > 2) {
            cout << "Too chaotic" << endl;
            return;
        }
        for (int j = max(0, q[i] - 2); j < i; j++)
            if (q[j] > q[i]) ans++;
    }
    cout << ans << endl;
}
