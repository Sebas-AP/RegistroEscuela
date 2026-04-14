import flet as ft

def get_agregar_view(page: ft.Page):
    page.padding = 0
    page.update()

    # Estilos compartidos
    label_style_yellow = dict(size=22, italic=True, weight=ft.FontWeight.W_800, color="#f1ac20")
    label_style_dark = dict(size=22, italic=True, weight=ft.FontWeight.W_800, color="#4d4a41")
    
    def MyTextField(width):
        return ft.Container(
            bgcolor="#a09d94",
            border_radius=20,
            width=width,
            height=45,
            padding=ft.padding.only(left=15, right=15),
            content=ft.TextField(
                border=ft.InputBorder.NONE,
                bgcolor=ft.Colors.TRANSPARENT,
                color=ft.Colors.BLACK87,
                cursor_color=ft.Colors.BLACK,
                expand=True
            )
        )

    # Controles
    btn_buscar = ft.ElevatedButton(
        content=ft.Text("Buscar", size=22, italic=True, weight=ft.FontWeight.W_900, color="#f0ece1"),
        style=ft.ButtonStyle(
            bgcolor="#eead2e",
            shape=ft.RoundedRectangleBorder(radius=20),
            padding=ft.padding.symmetric(horizontal=40, vertical=10),
        ),
        on_click=lambda e: print("Buscar click")
    )

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
                    padding=ft.padding.symmetric(horizontal=50, vertical=20),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            # Fila 1: CURP
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=20,
                                controls=[
                                    ft.Container(width=150, content=ft.Text("CURP", **label_style_yellow)),
                                    MyTextField(width=600),
                                    btn_buscar
                                ]
                            ),
                            # Fila 2: Escuela
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=20,
                                controls=[
                                    ft.Container(width=150, content=ft.Text("Escuela", **label_style_yellow)),
                                    MyTextField(width=600),
                                ]
                            ),
                            # Fila 3: Contenedor Grupo, Grado, Ciclo
                            ft.Container(
                                bgcolor="#cdc2a5", # Un tono ligeramente distinto
                                border_radius=30,
                                padding=ft.padding.symmetric(vertical=15, horizontal=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Row([ft.Text("Grupo", **label_style_dark), ft.Container(width=10), MyTextField(width=100)]),
                                        ft.Row([ft.Text("Grado", **label_style_dark), ft.Container(width=10), MyTextField(width=100)]),
                                        ft.Row([ft.Text("Ciclo", **label_style_dark), ft.Container(width=10), MyTextField(width=150)]),
                                    ]
                                )
                            ),
                            # Fila 4: Promedio, Folio
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        spacing=20,
                                        controls=[
                                            ft.Container(width=120, content=ft.Text("Promedio", **label_style_yellow)),
                                            MyTextField(width=250),
                                        ]
                                    ),
                                    ft.Row(
                                        spacing=20,
                                        controls=[
                                            ft.Text("Folio de certificado", **label_style_yellow),
                                            MyTextField(width=250),
                                        ]
                                    )
                                ]
                            ),
                            # Fila 5: Libro, Foja
                            ft.Container(
                                bgcolor="#cdc2a5",
                                border_radius=30,
                                padding=ft.padding.symmetric(vertical=15, horizontal=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        ft.Row([ft.Text("Libro", **label_style_dark), ft.Container(width=20), MyTextField(width=200)]),
                                        ft.Row([ft.Text("Foja", **label_style_dark), ft.Container(width=20), MyTextField(width=200)]),
                                    ]
                                )
                            ),
                            # Botón volver al menu opcional (por usabilidad, aunque no está en la imagen)
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextButton("Volver al Menú", on_click=lambda e: page.go("/menu"))
                                ]
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
