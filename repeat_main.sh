## Shellscript to repeatedly run "Main.PY" for all the sample texts to test
## out the logger module.

for (( i=1;i<=256;i++ ))
do
    echo "Iteration: $i."

    echo "$i.1 Reading Assamese Text"
    python main.py as_01.txt

    echo "$i.2 Reading English Blog"
    python main.py blog_01.txt

    echo "$i.3 Reading Hindi Blog"
    python main.py blog_02.txt

    echo "$i.4 Reading Marathi Blog"
    python main.py blog_03.txt

    echo "$i.5 Reading English Sample Text"
    python main.py en_01.txt

    echo "$i.6 Reading Japanese Sample Text"
    python main.py ja_01.txt

    echo "$i.7 Reading Korean Sample Text"
    python main.py ko_01.txt

    echo "$i.8 Reading Latin Sample Text"
    python main.py la_01.txt

    echo "$i.9 Reading Random Sample Text 1"
    python main.py random_01.txt

    echo "$i.10 Reading Sanskrit Sample Text"
    python main.py sa_01.txt

    echo "$i.11 Reading Mandarin-Chinese Sample Text"
    python main.py zh_01.txt
done