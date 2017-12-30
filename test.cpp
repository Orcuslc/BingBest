#include <QApplication>
#include <QWidget>

int main(int argc, char *argv[]) {

    QApplication app(argc, argv);

    QWidget w;
 	
 	w.setObjectName("main");
 	w.resize(400, 300);
	w.setStyleSheet("#main{border-image:url(./test.jpg);}");

	w.show();  
	w.move(200,100);

    return app.exec();
}
