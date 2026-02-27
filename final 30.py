{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO6BX2IWFjYrxLbhrWavX2q",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Boonsita30/30-Coding68/blob/main/final%2030.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"💗🌸\" + \"═\"*40 + \"🌸💗\")\n",
        "print(\"💖      โปรแกรมคำนวณค่าไฟฟ้า      💖\")\n",
        "print(\"💗🌸\" + \"═\"*40 + \"🌸💗\")\n",
        "\n",
        "name = input(\"🌷 ยินดีต้อนรับเข้าสู่โปรแกรมคำนวณค่าไฟฟ้าค่ะ\\n💞 ผู้ใช้ชื่ออะไรคะ: \")\n",
        "\n",
        "print(\"\\n🌸 กรุณากรอกจำนวนหน่วยค่าไฟ 🌸\")\n",
        "unit1 = int(input(\"💗 ใส่เลข 1-25: \"))\n",
        "unit2 = int(input(\"💗 ใส่เลข 1-30: \"))\n",
        "\n",
        "total = unit1 + unit2\n",
        "\n",
        "print(\"\\n💖🌷\" + \"─\"*40 + \"🌷💖\")\n",
        "print(f\"🌸 คุณ {name} ใช้ไฟฟ้ารวมทั้งหมด: {total} หน่วย 💕\")\n",
        "\n",
        "if total <= 50:\n",
        "    print(\"💗 ค่าไฟฟ้าของคุณ หน่วยละ 2.50 บาท 🌷\")\n",
        "else:\n",
        "    print(\"💗 ค่าไฟฟ้าของคุณ หน่วยละ 5.00 บาท 🌷\")\n",
        "\n",
        "print(\"💖🌸\" + \"═\"*40 + \"🌸💖\")\n",
        "print(\"💞 ขอบคุณที่ใช้บริการค่ะ 💞\")\n",
        "print(\"💗🌸\" + \"═\"*40 + \"🌸💗\")\n",
        "\n",
        "print(\"cr.Boonsita 30\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yn-Sg6EE7KXn",
        "outputId": "92ad6af3-3db8-438a-f2e2-febc557e5ef7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "💗🌸════════════════════════════════════════🌸💗\n",
            "💖      โปรแกรมคำนวณค่าไฟฟ้า      💖\n",
            "💗🌸════════════════════════════════════════🌸💗\n",
            "🌷 ยินดีต้อนรับเข้าสู่โปรแกรมคำนวณค่าไฟฟ้าค่ะ\n",
            "💞 ผู้ใช้ชื่ออะไรคะ: ใบบัว\n",
            "\n",
            "🌸 กรุณากรอกจำนวนหน่วยค่าไฟ 🌸\n",
            "💗 ใส่เลข 1-25: 20\n",
            "💗 ใส่เลข 1-30: 26\n",
            "\n",
            "💖🌷────────────────────────────────────────🌷💖\n",
            "🌸 คุณ ใบบัว ใช้ไฟฟ้ารวมทั้งหมด: 46 หน่วย 💕\n",
            "💗 ค่าไฟฟ้าของคุณ หน่วยละ 2.50 บาท 🌷\n",
            "💖🌸════════════════════════════════════════🌸💖\n",
            "💞 ขอบคุณที่ใช้บริการค่ะ 💞\n",
            "💗🌸════════════════════════════════════════🌸💗\n",
            "cr.Boonsita 30\n"
          ]
        }
      ]
    }
  ]
}