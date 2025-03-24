echo "Starting LibreTranslate"
libretranslate &
sleep 5

cd py-files
echo "Starting Flask API"
python main.py &
sleep 5

cd ..

cd road-sign-translator
echo "Starting Road Sign Translator App"
npm run ios