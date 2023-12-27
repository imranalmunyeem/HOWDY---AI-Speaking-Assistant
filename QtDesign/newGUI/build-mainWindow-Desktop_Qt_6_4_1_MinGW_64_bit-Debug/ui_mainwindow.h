/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QLabel *videoLabel;
    QLabel *kartisTechLabel;
    QLabel *label;
    QPushButton *LoginButton_3;
    QPushButton *LoginButton_2;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(1080, 720);
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        videoLabel = new QLabel(centralwidget);
        videoLabel->setObjectName("videoLabel");
        videoLabel->setGeometry(QRect(5, 100, 640, 480));
        videoLabel->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);\n"
"font:18pt \"Karisma\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px 1px 1px 1px;\n"
"border-radius: 20px;"));
        kartisTechLabel = new QLabel(centralwidget);
        kartisTechLabel->setObjectName("kartisTechLabel");
        kartisTechLabel->setGeometry(QRect(240, 10, 640, 81));
        kartisTechLabel->setStyleSheet(QString::fromUtf8("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"));
        kartisTechLabel->setPixmap(QPixmap(QString::fromUtf8("../../../gui_tools/KartisTechnology(white).png")));
        kartisTechLabel->setScaledContents(true);
        label = new QLabel(centralwidget);
        label->setObjectName("label");
        label->setEnabled(true);
        label->setGeometry(QRect(730, -40, 481, 761));
        label->setPixmap(QPixmap(QString::fromUtf8("../../../gui_tools/ironman-portrait.webp")));
        label->setScaledContents(true);
        LoginButton_3 = new QPushButton(centralwidget);
        LoginButton_3->setObjectName("LoginButton_3");
        LoginButton_3->setGeometry(QRect(89, 600, 231, 101));
        LoginButton_3->setCursor(QCursor(Qt::PointingHandCursor));
        LoginButton_3->setStyleSheet(QString::fromUtf8("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/login-empty.png);\n"
"background:transparent;"));
        LoginButton_3->setFlat(false);
        LoginButton_2 = new QPushButton(centralwidget);
        LoginButton_2->setObjectName("LoginButton_2");
        LoginButton_2->setGeometry(QRect(320, 602, 231, 101));
        LoginButton_2->setCursor(QCursor(Qt::PointingHandCursor));
        LoginButton_2->setStyleSheet(QString::fromUtf8("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/exit.png);\n"
"background:transparent;"));
        LoginButton_2->setFlat(false);
        MainWindow->setCentralWidget(centralwidget);
        videoLabel->raise();
        label->raise();
        kartisTechLabel->raise();
        LoginButton_3->raise();
        LoginButton_2->raise();

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        videoLabel->setText(QCoreApplication::translate("MainWindow", "<html><head/><body><p align=\"center\">If you read this, then there is something wrong with your Web Camera!</p></body></html>", nullptr));
        kartisTechLabel->setText(QString());
        label->setText(QString());
        LoginButton_3->setText(QString());
        LoginButton_2->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
