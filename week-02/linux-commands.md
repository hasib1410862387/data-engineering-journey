
grep "| ERROR |" app.log | cut -c1-10 | sort | uniq -c | sort -rn
grep "| ERROR |" app.log > errors.log
echo "আেরকটা লাইন" >> errors.log
