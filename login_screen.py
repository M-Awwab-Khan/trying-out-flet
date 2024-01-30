import flet as ft

def main(page):
    page.title = "Card Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Row(controls=[ft.Text("Log In", weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.DISPLAY_SMALL, text_align=ft.TextAlign.CENTER)], alignment=ft.MainAxisAlignment.CENTER),
                        ft.TextField(label="Username", border_width=0.5, focused_border_width=0.7),
                        ft.TextField(label="Password", border_width=0.5, focused_border_width=0.7, password=True, can_reveal_password=True),
                        ft.Row(
                            controls=[ft.FloatingActionButton(
                                content=ft.Row(
                                    [ft.Icon(ft.icons.PERSON_ROUNDED), ft.Text("Sign in")], alignment="center", spacing=5
                                ),
                                bgcolor=ft.colors.INVERSE_PRIMARY,
                                shape=ft.RoundedRectangleBorder(radius=10),
                                width=150,
                                mini=True,
                            )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=30
                ),
                width=400,
                padding=40,
            ),
        )
    )

ft.app(target=main)
