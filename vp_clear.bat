@echo off
setlocal

REM Đặt danh sách các ổ đĩa bạn muốn quét
set "drives=C D F"

REM Đặt danh sách các phần mở rộng tệp bạn muốn liệt kê và xóa
set "extensions=.sfk .sfl .sfap0 .sfvp0 .veg.bak"

REM Lặp qua các ổ đĩa
for %%D in (%drives%) do (
    echo Scanning drive %%D:

    REM Di chuyển đến ổ đĩa
    cd /d "%%D:\"

    REM Liệt kê tất cả các tệp có phần mở rộng được chỉ định
    for /r %%F in (*.sfk *.sfl *.sfap0 *.sfvp0 *.veg.bak) do (
        echo File: "%%F"
    )

    echo.

    REM Xóa tất cả các tệp có phần mở rộng được chỉ định
    for /r %%F in (*.sfk *.sfl *.sfap0 *.sfvp0 *.veg.bak) do (
        echo Delete: "%%F"
        del "%%F"
    )
)

pause
