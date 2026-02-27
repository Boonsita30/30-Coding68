{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMMIz89U0XWppnbpqd+xEvo",
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
        "<a href=\"https://colab.research.google.com/github/Boonsita30/30-Coding68/blob/main/final30.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name=input(\"ยินดีต้อนรับเข้าสู่โปรแกมคำนวณค่าไฟฟ้าค่ะ ผู้ใช้ชื่ออะไรค่ะ\\n\")\n",
        "\n",
        "print(\"กรุณากรอกจำนวนหน่วยค่าไฟ\")\n",
        "unit1=int(input(\"ใส่เลขระหว่าง1-25: \"))\n",
        "unit2=int(input(\"ใส่เลขระหว่าง1-30: \"))\n",
        "\n",
        "total = unit1 + unit2\n",
        "\n",
        "print(\"\\nรวมค่าไฟฟ้าทั้งหมด:\", total )\n",
        "\n",
        "if total<=50:\n",
        "  print(\"ค่าไฟฟ้าของคุณหน่วยละ 2.50 บาทต่ะ\")\n",
        "elif total > 50:\n",
        "  print(\"ค่าไฟฟ้าของคุณหน่วยละ 5.00 บาทค่ะ\")\n",
        "\n",
        "print(\"การคำนวณของคุณสำเร็จแล้วค่ะ\")\n",
        "print(\"cr.Boonsita30\\n\")"
      ],
      "metadata": {
        "id": "KOdbA15AbcZ4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "05b755b3-0b82-4825-974a-1c29f3e9bf79"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ยินดีต้อนรับเข้าสู่โปรแกมคำนวณค่าไฟฟ้าค่ะ ผู้ใช้ชื่ออะไรค่ะ\n",
            "ใบบัว\n",
            "กรุณากรอกจำนวนหน่วยค่าไฟ\n",
            "ใส่เลขระหว่าง1-25: 25\n",
            "ใส่เลขระหว่าง1-30: 22\n",
            "\n",
            "รวมค่าไฟฟ้าทั้งหมด: 47\n",
            "ค่าไฟฟ้าของคุณหน่วยละ 2.50 บาทต่ะ\n",
            "การคำนวณของคุณสำเร็จแล้วค่ะ\n",
            "cr.Boonsita30\n",
            "\n"
          ]
        }
      ]
    }
  ]
}