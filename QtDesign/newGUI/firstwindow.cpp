#include "firstwindow.h"
#include "ui_firstwindow.h"

firstWindow::firstWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::firstWindow)
{
    ui->setupUi(this);
}

firstWindow::~firstWindow()
{
    delete ui;
}

