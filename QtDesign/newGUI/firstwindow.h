#ifndef FIRSTWINDOW_H
#define FIRSTWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class firstWindow; }
QT_END_NAMESPACE

class firstWindow : public QMainWindow
{
    Q_OBJECT

public:
    firstWindow(QWidget *parent = nullptr);
    ~firstWindow();

private:
    Ui::firstWindow *ui;
};
#endif // FIRSTWINDOW_H
