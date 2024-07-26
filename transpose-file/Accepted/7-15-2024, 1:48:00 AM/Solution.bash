// https://leetcode.com/problems/transpose-file

# Read from the file file.txt and print its transposed content to stdout.
num_cols=$(head -n1 file.txt | wc -w)
for (( i=1; i<=num_cols; i++ )); do
    cut -d' ' -f$i file.txt | paste -s -d ' '
done