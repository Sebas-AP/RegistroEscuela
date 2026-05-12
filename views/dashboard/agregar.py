import flet as ft
from core.database import get_supabase_client

def get_agregar_view(page: ft.Page):
    page.padding = 0
    page.update()

    supabase = get_supabase_client()

    label_style_yellow = dict(size=22, italic=True, weight=ft.FontWeight.W_800, color="#f1ac20")
    label_style_dark = dict(size=22, italic=True, weight=ft.FontWeight.W_800, color="#4d4a41")

    def MyTextField(width):
        return ft.Container(
            bgcolor="#a09d94",
            border_radius=20,
            width=width,
            height=45,
            padding=ft.Padding.only(left=15, right=15),
            content=ft.TextField(
                border=ft.InputBorder.NONE,
                bgcolor=ft.Colors.TRANSPARENT,
                color=ft.Colors.BLACK87,
                cursor_color=ft.Colors.BLACK,
                expand=True
            )
        )

    cst_field = MyTextField(width=200)
    nombre_esc_field = MyTextField(width=450)
    localidad_field = MyTextField(width=200)
    zona_field = MyTextField(width=150)

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Row([
            ft.Text("Agregar Escuela", size=30, italic=True, weight=ft.FontWeight.W_900, color="#5c000b", text_align=ft.TextAlign.CENTER, expand=True),
            ft.IconButton(icon="close", icon_size=30, on_click=lambda e: page.pop_dialog(), icon_color="#5c000b")
        ]),
        content=ft.Container(
            width=650,
            height=250,
            padding=5,
            content=ft.Column([
                ft.Row([
                    ft.Container(width=100, content=ft.Text("CST", size=18, italic=True, weight=ft.FontWeight.W_800, color="#4d4a41", text_align=ft.TextAlign.RIGHT)),
                    cst_field,
                    ft.Container(expand=True),
                    ft.ElevatedButton(
                        "Guardar",
                        style=ft.ButtonStyle(bgcolor="#5c000b", color="#dcdad0", shape=ft.RoundedRectangleBorder(radius=15), padding=ft.Padding.symmetric(horizontal=30, vertical=15)),
                        on_click=lambda e: print("Guardar escuela")
                    )
                ], alignment=ft.MainAxisAlignment.START),
                ft.Container(height=10),
                ft.Row([
                    ft.Container(width=100, content=ft.Text("Nombre", size=18, italic=True, weight=ft.FontWeight.W_800, color="#4d4a41", text_align=ft.TextAlign.RIGHT)),
                    nombre_esc_field
                ]),
                ft.Container(height=10),
                ft.Row([
                    ft.Container(width=100, content=ft.Text("Localidad", size=18, italic=True, weight=ft.FontWeight.W_800, color="#4d4a41", text_align=ft.TextAlign.RIGHT)),
                    localidad_field,
                    ft.Text("Zona", size=18, italic=True, weight=ft.FontWeight.W_800, color="#4d4a41"),
                    zona_field
                ], alignment=ft.MainAxisAlignment.START),
                ft.Container(height=10),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                    controls=[
                        ft.ElevatedButton(
                            "Cerrar",
                            style=ft.ButtonStyle(bgcolor="#7b7971", color="#dcdad0", shape=ft.RoundedRectangleBorder(radius=15), padding=ft.Padding.symmetric(horizontal=30, vertical=12)),
                            on_click=lambda e: page.pop_dialog()
                        )
                    ]
                )
            ])
        ),
        bgcolor="#cdc2a5",
        shape=ft.RoundedRectangleBorder(radius=30)
    )

    def open_dlg(e):
        page.show_dialog(dlg_modal)

    btn_buscar = ft.ElevatedButton(
        content=ft.Text("Buscar", size=22, italic=True, weight=ft.FontWeight.W_900, color="#f0ece1"),
        style=ft.ButtonStyle(
            bgcolor="#eead2e",
            shape=ft.RoundedRectangleBorder(radius=20),
            padding=ft.Padding.symmetric(horizontal=40, vertical=10),
        ),
        on_click=lambda e: print("Buscar click")
    )

    btn_agregar_escuela = ft.ElevatedButton(
        "Agregar Escuela",
        style=ft.ButtonStyle(
            bgcolor="#5c000b",
            color="#dcdad0",
            shape=ft.RoundedRectangleBorder(radius=20),
            padding=ft.Padding.symmetric(horizontal=20, vertical=12)
        ),
        on_click=open_dlg
    )

    return ft.Container(
        expand=True,
        bgcolor="#d1ccbc",
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    height=90,
                    padding=ft.Padding.symmetric(horizontal=30),
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
                ft.Container(
                    expand=True,
                    padding=ft.Padding.symmetric(horizontal=50, vertical=20),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=20,
                                controls=[
                                    ft.Container(width=150, content=ft.Text("CURP", **label_style_yellow)),
                                    MyTextField(width=600),
                                    btn_buscar
                                ]
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                spacing=20,
                                controls=[
                                    ft.Container(width=150, content=ft.Text("Escuela", **label_style_yellow)),
                                    ft.Container(
                                        bgcolor="#a09d94",
                                        border_radius=20,
                                        width=350,
                                        height=45,
                                        padding=ft.Padding.only(left=15, right=15),
                                        content=ft.Dropdown(
                                            border=ft.InputBorder.NONE,
                                            color=ft.Colors.BLACK87,
                                            options=[
                                                ft.dropdown.Option("Seleccionar escuela..."),
                                            ],
                                        )
                                    ),
                                    btn_agregar_escuela
                                ]
                            ),
                            ft.Container(
                                bgcolor="#cdc2a5",
                                border_radius=30,
                                padding=ft.Padding.symmetric(vertical=15, horizontal=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Row([ft.Text("Grupo", **label_style_dark), ft.Container(width=10), MyTextField(width=100)]),
                                        ft.Row([ft.Text("Grado", **label_style_dark), ft.Container(width=10), MyTextField(width=100)]),
                                        ft.Row([ft.Text("Ciclo", **label_style_dark), ft.Container(width=10), MyTextField(width=150)]),
                                    ]
                                )
                            ),
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
                            ft.Container(
                                bgcolor="#cdc2a5",
                                border_radius=30,
                                padding=ft.Padding.symmetric(vertical=15, horizontal=30),
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        ft.Row([ft.Text("Libro", **label_style_dark), ft.Container(width=20), MyTextField(width=200)]),
                                        ft.Row([ft.Text("Foja", **label_style_dark), ft.Container(width=20), MyTextField(width=200)]),
                                    ]
                                )
                            ),
                            ft.ElevatedButton(
                                "Volver al Menú",
                                style=ft.ButtonStyle(
                                    bgcolor="#5c000b",
                                    color="#dcdad0",
                                    shape=ft.RoundedRectangleBorder(radius=20),
                                    padding=ft.Padding.symmetric(horizontal=20, vertical=12)
                                ),
                                on_click=lambda e: page.go("/menu")
                            )
                        ]
                    )
                ),
                ft.Container(
                    height=70,
                    padding=ft.Padding.only(right=30, top=5, bottom=5),
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