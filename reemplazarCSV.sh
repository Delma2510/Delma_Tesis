(echo "DatetimeFull"; cat "/home/delma/Desktop/Versiones/Catalogos_csv/catalogo.csv") | sed 's/"//g' > "/home/delma/Desktop/Versiones/Catalogo_txt/catalogo.txt"
sed -i "s/+20s/+120s/g" "/home/delma/Desktop/Versiones/Catalogo_txt/catalogo.txt"
sed -i "1,2d" "/home/delma/Desktop/Versiones/Catalogo_txt/catalogo.txt"

(echo "DatetimeFull"; cat "/home/delma/Desktop/Versiones/Catalogos_csv/notec.csv") | sed 's/"//g' > "/home/delma/Desktop/Versiones/Catalogo_txt/notec.txt"
sed -i "1,2d" "/home/delma/Desktop/Versiones/Catalogo_txt/notec.txt"

(echo "DatetimeFull"; cat "/home/delma/Desktop/Versiones/Catalogos_csv/tec.csv") | sed 's/"//g' > "/home/delma/Desktop/Versiones/Catalogo_txt/tec.txt"
sed -i "1,2d" "/home/delma/Desktop/Versiones/Catalogo_txt/tec.txt"


