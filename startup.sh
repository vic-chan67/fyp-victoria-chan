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
# export EXPO_DEVTOOLS_LISTEN_ADDRESS=localhost
# npm run ios -- --localhost

npm run ios
