def build_instruction(
        goal: str,
        rules: list[str],
        output_format: str,
) -> str:
    try:
        goal = goal.strip()
        output_format = output_format.strip()
    except:
        raise TypeError from None
    if not goal or not output_format:
        raise ValueError

    if not isinstance(rules, list):
        raise TypeError

    if not rules:
        raise ValueError

    try:
        cleaned_rules = ["- " + s.strip() for s in rules if s.strip()]
    except:
        raise TypeError from None

    if len(cleaned_rules) < len(rules):
        raise ValueError

    goal = f"Цель:\n{goal}"
    cleaned_rules = f"\nПравила:\n{"\n".join(cleaned_rules)}"
    output_format = f"\nФормат ответа:\n{output_format}"

    return f"{goal}\n{cleaned_rules}\n{output_format}"


print(build_instruction(
    "Кратко перескажи обращение.",
    ["Не добавляй факты.", "Не давай советов.", "   "],
    "Одно предложение.",
))