import flet as ft
from core.database import get_supabase_client

def get_register_view(page: ft.Page):
    supabase = get_supabase_client()
    
    txt_name = ft.TextField(label="Nombre Completo", width=300, prefix_icon="badge")
    txt_usu = ft.TextField(label="Nombre de Usuario", width=300, prefix_icon="person")
    txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, prefix_icon="lock")

    def show_snack(message, color=ft.Colors.RED_400):
        snack = ft.SnackBar(content=ft.Text(message), bgcolor=color)
        page.overlay.append(snack)
        snack.open = True
        page.update()

    def on_register_click(e):
        if not txt_name.value or not txt_usu.value or not txt_pass.value:
            show_snack("Por favor llena todos los campos")
            return
        if not supabase:
            show_snack("Sin conexión a BD", ft.Colors.ORANGE_500)
            return
        try:
            data = {"name": txt_name.value, "nameUsu": txt_usu.value, "pass": txt_pass.value, "role": 1}
            supabase.table("usuarios").insert(data).execute()
            show_snack("Registrado exitosamente", ft.Colors.GREEN_500)
            page.go("/login")
        except Exception as ex:
            show_snack(f"Error al registrar: {ex}")

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Registro", size=32, weight=ft.FontWeight.BOLD),
                txt_name,
                txt_usu,
                txt_pass,
                ft.Container(height=10),
                ft.ElevatedButton("Registrarse", icon="person_add", on_click=on_register_click),
                ft.TextButton("Regresar a Iniciar Sesión", on_click=lambda e: page.go("/login"))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.Alignment.CENTER,
        expand=True
    )
