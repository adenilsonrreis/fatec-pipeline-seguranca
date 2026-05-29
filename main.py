def verificar_peso_carga(peso: float) -> str:
    """Valida se o peso da carga está dentro do limite seguro."""
    if not isinstance(peso, (int, float)):
        raise TypeError("O peso deve ser um valor numérico")
    if peso <= 0:
        raise ValueError("Peso deve ser maior que zero")
    if peso > 20.0:
        return "Carga Excedida! Risco de seguranca."
    return "Peso dentro do limite seguro."

if __name__ == "__main__":
    print(verificar_peso_carga(12.5))