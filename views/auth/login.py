import flet as ft
from core.database import get_supabase_client

def get_login_view(page: ft.Page):
    # Aseguramos que la página no tenga padding para que el fondo cubra todo
    page.padding = 0
    page.update()
    
    supabase = get_supabase_client()
    
    txt_usu = ft.TextField(
        border=ft.InputBorder.NONE,
        bgcolor=ft.Colors.TRANSPARENT,
        color=ft.Colors.BLACK87,
        cursor_color=ft.Colors.BLACK,
        expand=True
    )
    
    txt_pass = ft.TextField(
        border=ft.InputBorder.NONE,
        bgcolor=ft.Colors.TRANSPARENT,
        color=ft.Colors.BLACK87,
        cursor_color=ft.Colors.BLACK,
        password=True,
        can_reveal_password=True,
        expand=True
    )
    
    def show_snack(message, color=ft.Colors.RED_400):
        snack = ft.SnackBar(content=ft.Text(message), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def on_login_click(e):
        if not txt_usu.value or not txt_pass.value:
            show_snack("Por favor llena todos los campos")
            return
        if not supabase:
            show_snack("Sin conexión a BD", ft.Colors.ORANGE_500)
            return
        try:
            res = supabase.table("usuarios").select("*").eq("nameUsu", txt_usu.value).eq("pass", txt_pass.value).execute()
            if res.data and len(res.data) > 0:
                show_snack(f"¡Bienvenido {res.data[0].get('name')}!", ft.Colors.GREEN_500)
                # Redirect to dashboard upon successful login
                page.go("/menu")
            else:
                show_snack("Credenciales incorrectas")
        except Exception as ex:
            show_snack(f"Error BD: {ex}")

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
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.Image(src="src/img/logoSHIS_sinFondo.png", height=150, fit="contain"),
                            ft.Container(height=10),
                            
                            # Usuario Label and Input
                            ft.Column(
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Usuario", size=22, italic=True, weight=ft.FontWeight.W_800, color="#f1ac20"),
                                    ft.Container(
                                        bgcolor="#a09d94",
                                        border_radius=30,
                                        width=450,
                                        height=60,
                                        padding=ft.padding.only(left=20, right=10, top=5),
                                        content=ft.Row([txt_usu], expand=True)
                                    )
                                ]
                            ),
                            ft.Container(height=5),
                            # Contraseña Label and Input
                            ft.Column(
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Contraseña", size=22, italic=True, weight=ft.FontWeight.W_800, color="#f1ac20"),
                                    ft.Container(
                                        bgcolor="#a09d94",
                                        border_radius=30,
                                        width=450,
                                        height=60,
                                        padding=ft.padding.only(left=20, right=10, top=5),
                                        content=ft.Row([txt_pass], expand=True)
                                    )
                                ]
                            ),
                            ft.Container(height=30),
                            # Buttons
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=40,
                                controls=[
                                    ft.ElevatedButton(
                                        content=ft.Text("Registrar", size=22, italic=True, weight=ft.FontWeight.W_900, color="#374149"),
                                        style=ft.ButtonStyle(
                                            bgcolor="#eead2e",
                                            shape=ft.RoundedRectangleBorder(radius=30),
                                            padding=ft.padding.symmetric(horizontal=40, vertical=20),
                                        ),
                                        on_click=lambda e: page.go("/register")
                                    ),
                                    ft.ElevatedButton(
                                        content=ft.Text("Iniciar", size=22, italic=True, weight=ft.FontWeight.W_900, color="#374149"),
                                        style=ft.ButtonStyle(
                                            bgcolor="#eead2e",
                                            shape=ft.RoundedRectangleBorder(radius=30),
                                            padding=ft.padding.symmetric(horizontal=50, vertical=20),
                                        ),
                                        on_click=on_login_click
                                    )
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
