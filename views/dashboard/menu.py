import flet as ft

def get_menu_view(page: ft.Page):
    page.padding = 0
    page.update()

    def on_consultar_click(e):
        page.go("/dashboard")

    def on_agregar_click(e):
        page.go("/agregar")

    return ft.Container(
        expand=True,
        bgcolor="#d1ccbc",
        content=ft.Column(
            spacing=0,
            controls=[
                # Top Bar
                ft.Container(
                    height=90,
                    padding=ft.padding.symmetric(horizontal=30),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment.CENTER_LEFT,
                        end=ft.Alignment.CENTER_RIGHT,
                        colors=["#7b7971", "#9f9d92", "#b1afa3"]
                    ),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("SIHIS", size=45, italic=True, weight=ft.FontWeight.W_900, color="#dcdad0"),
                            ft.Image(src="src/img/logoSHIS_sinFondo.png", height=70, fit="contain")
                        ]
                    )
                ),
                # Center Content
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=80,
                        controls=[
                            # Botón Consultar
                            ft.Container(
                                width=250,
                                height=220,
                                bgcolor="#5c000b", # Oscuro rojizo
                                border_radius=40,
                                alignment=ft.Alignment.CENTER,
                                on_click=on_consultar_click,
                                ink=True,
                                content=ft.Text("Consultar", size=32, italic=True, weight=ft.FontWeight.W_900, color="#dcdad0")
                            ),
                            # Botón Agregar
                            ft.Container(
                                width=250,
                                height=220,
                                bgcolor="#eead2e", # Amarillo mostaza
                                border_radius=40,
                                alignment=ft.Alignment.CENTER,
                                on_click=on_agregar_click,
                                ink=True,
                                content=ft.Text("Agregar", size=32, italic=True, weight=ft.FontWeight.W_900, color="#dcdad0")
                            )
                        ]
                    )
                ),
                # Bottom Bar
                ft.Container(
                    height=70,
                    padding=ft.padding.only(right=30, top=5, bottom=5),
                    bgcolor="#9e9c93",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Image(src="src/img/logoSHIS_sinFondo.png", height=50, fit="contain")
                        ]
                    )
                )
            ]
        )
    )
