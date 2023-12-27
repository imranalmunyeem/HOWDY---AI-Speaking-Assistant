/********************************************************************************
** Form generated from reading UI file 'loginwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.4.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LOGINWINDOW_H
#define UI_LOGINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_loginWindow
{
public:
    QWidget *centralwidget;
    QFrame *loginmainFrame;
    QPushButton *LoginButton;
    QLineEdit *passwordEdit;
    QLineEdit *usernameEdit;
    QPushButton *LoginButton_2;
    QPushButton *LoginButton_3;
    QPushButton *retryButton;
    QLabel *kartisTechLabel;

    void setupUi(QMainWindow *loginWindow)
    {
        if (loginWindow->objectName().isEmpty())
            loginWindow->setObjectName("loginWindow");
        loginWindow->resize(1080, 725);
        loginWindow->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        centralwidget = new QWidget(loginWindow);
        centralwidget->setObjectName("centralwidget");
        loginmainFrame = new QFrame(centralwidget);
        loginmainFrame->setObjectName("loginmainFrame");
        loginmainFrame->setGeometry(QRect(180, 55, 721, 661));
        loginmainFrame->setAutoFillBackground(false);
        loginmainFrame->setStyleSheet(QString::fromUtf8("border-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 5px 5px 5px 5px;\n"
"border-radius: 30px;"));
        loginmainFrame->setFrameShape(QFrame::StyledPanel);
        loginmainFrame->setFrameShadow(QFrame::Raised);
        LoginButton = new QPushButton(loginmainFrame);
        LoginButton->setObjectName("LoginButton");
        LoginButton->setGeometry(QRect(208, 358, 274, 101));
        LoginButton->setCursor(QCursor(Qt::PointingHandCursor));
        LoginButton->setStyleSheet(QString::fromUtf8("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/login.png);\n"
"background: transparent;"));
        LoginButton->setFlat(false);
        passwordEdit = new QLineEdit(loginmainFrame);
        passwordEdit->setObjectName("passwordEdit");
        passwordEdit->setGeometry(QRect(150, 268, 391, 71));
        passwordEdit->setStyleSheet(QString::fromUtf8("border-color: rgb(255, 255, 255);\n"
"font: 30pt \"IRON MAN OF WAR 2 NCV\";\n"
"border-style: solid;\n"
"border-width: 1px 1px 1px 1px;\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255)"));
        usernameEdit = new QLineEdit(loginmainFrame);
        usernameEdit->setObjectName("usernameEdit");
        usernameEdit->setGeometry(QRect(150, 168, 391, 71));
        usernameEdit->setStyleSheet(QString::fromUtf8("border-color: rgb(255, 255, 255);\n"
"font: 30pt \"IRON MAN OF WAR 2 NCV\";\n"
"border-style: solid;\n"
"border-width: 1px 1px 1px 1px;\n"
"border-radius: 20px;\n"
"color:rgb(255, 255, 255);\n"
"background: transparent;"));
        LoginButton_2 = new QPushButton(loginmainFrame);
        LoginButton_2->setObjectName("LoginButton_2");
        LoginButton_2->setGeometry(QRect(460, 540, 201, 91));
        LoginButton_2->setCursor(QCursor(Qt::PointingHandCursor));
        LoginButton_2->setStyleSheet(QString::fromUtf8("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/exit.png);\n"
"background: transparent;"));
        LoginButton_2->setFlat(false);
        LoginButton_3 = new QPushButton(loginmainFrame);
        LoginButton_3->setObjectName("LoginButton_3");
        LoginButton_3->setGeometry(QRect(260, 535, 201, 91));
        LoginButton_3->setCursor(QCursor(Qt::PointingHandCursor));
        LoginButton_3->setStyleSheet(QString::fromUtf8("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/back.png);\n"
"background: transparent;"));
        LoginButton_3->setFlat(false);
        retryButton = new QPushButton(loginmainFrame);
        retryButton->setObjectName("retryButton");
        retryButton->setGeometry(QRect(60, 543, 200, 81));
        retryButton->setCursor(QCursor(Qt::PointingHandCursor));
        retryButton->setStyleSheet(QString::fromUtf8("border-image: url(E:/CODING/Artificial_Intelligence/FacialRecogByJARVIS/with GUI/gui_tools/retry.png);\n"
"background: transparent;"));
        retryButton->setFlat(false);
        kartisTechLabel = new QLabel(loginmainFrame);
        kartisTechLabel->setObjectName("kartisTechLabel");
        kartisTechLabel->setGeometry(QRect(60, 40, 640, 81));
        kartisTechLabel->setStyleSheet(QString::fromUtf8("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border:none;"));
        kartisTechLabel->setPixmap(QPixmap(QString::fromUtf8("../../../gui_tools/KartisTechnology(white).png")));
        kartisTechLabel->setScaledContents(true);
        loginWindow->setCentralWidget(centralwidget);

        retranslateUi(loginWindow);

        QMetaObject::connectSlotsByName(loginWindow);
    } // setupUi

    void retranslateUi(QMainWindow *loginWindow)
    {
        loginWindow->setWindowTitle(QCoreApplication::translate("loginWindow", "Login", nullptr));
        LoginButton->setText(QString());
        passwordEdit->setPlaceholderText(QCoreApplication::translate("loginWindow", "Password", nullptr));
        usernameEdit->setPlaceholderText(QCoreApplication::translate("loginWindow", "Username", nullptr));
        LoginButton_2->setText(QString());
        LoginButton_3->setText(QString());
        retryButton->setText(QString());
        kartisTechLabel->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class loginWindow: public Ui_loginWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LOGINWINDOW_H
