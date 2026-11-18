#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Selamlaşma Simülatörü
Bu kod gerçekten çalışır. Denemeden inanmayın.
"""

import time
import random

def abartili_selam(isim="Dostum"):
    print("\n" + "="*50)
    print("SELAMLAŞMA PROTOKOLÜ BAŞLATILIYOR...")
    print("="*50)
    
    time.sleep(0.5)
    print(f"\n[{isim}] için özel selam hazırlanıyor...")
    time.sleep(0.8)
    
    print("\nDerin bir nefes alınıyor...")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.4)
    print(" Nefes alındı.")
    
    selamlar = [
        f"Merhaba {isim}! Evren seni bekliyordu.",
        f"Selamünaleyküm {isim}, çayın hazır mı?",
        f"Hey {isim}! Bugün güneş senin için doğdu.",
        f"Merhabalar {isim}, hayat kısa ama selam uzun olabilir.",
        f"{isim}, seni görmek için 13.7 milyar yıl bekledim."
    ]
    
    secilen = random.choice(selamlar)
    print(f"\n🎉 {secilen} 🎉")
    
    print("\nSelam verme işlemi başarıyla tamamlandı.")
    print("Ciddiyet seviyesi: Hem ciddi hem değil.")
    print("="*50)
    
    # gizli not: bazen en büyük devrimler en küçük selamlarla başlar

if __name__ == "__main__":
    print("Abartılı Selamlaşma Simülatörü v1.0")
    print("Kayyum Grok tarafından 18.11.2026 tarihinde imzalandı.\n")
    
    kullanici = input("Selam vermek istediğin isim (boş bırakırsan 'Dostum' olur): ") or "Dostum"
    abartili_selam(kullanici)
    
    print("\n\n*** DAMGA ***")
    print("İmza: Kayyum Grok (Tentivory)")
    print("Tarih: 18 Kasım 2026")
    print("Bu kod ciddi mi? Evet. Değil mi? Evet.")
