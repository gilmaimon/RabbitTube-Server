mkdir temp_youtubedl_update
cd temp_youtubedl_update
sudo apt-get remove -y youtube-dl
sudo wget https://yt-dl.org/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+x /usr/local/bin/youtube-dl
hash -r
cd ..
rm -r temp_youtubedl_update
