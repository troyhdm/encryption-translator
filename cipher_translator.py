#!/usr/bin/env python3
"""
Cipher/Encryption Translator
A tool to encode and decode messages using various cipher methods
"""

import string
import json
from typing import Dict, Tuple

class CipherTranslator:
    """Main cipher translator class with multiple cipher methods"""
    
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.digits = string.digits
    
    # ==================== CAESAR CIPHER ====================
    def caesar_encode(self, text: str, shift: int = 3) -> str:
        """Encode text using Caesar cipher"""
        result = []
        for char in text.lower():
            if char in self.alphabet:
                new_index = (self.alphabet.index(char) + shift) % 26
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return ''.join(result)
    
    def caesar_decode(self, text: str, shift: int = 3) -> str:
        """Decode text using Caesar cipher"""
        return self.caesar_encode(text, -shift)
    
    # ==================== ROT13 CIPHER ====================
    def rot13_encode(self, text: str) -> str:
        """Encode using ROT13 (Caesar with shift of 13)"""
        return self.caesar_encode(text, 13)
    
    def rot13_decode(self, text: str) -> str:
        """Decode ROT13 (same as encode since shift is 13)"""
        return self.rot13_encode(text)
    
    # ==================== SUBSTITUTION CIPHER ====================
    def substitution_encode(self, text: str, key: str = None) -> Tuple[str, str]:
        """Encode using substitution cipher with random or provided key"""
        if key is None:
            key = self._generate_substitution_key()
        
        mapping = dict(zip(self.alphabet, key))
        result = []
        for char in text.lower():
            if char in mapping:
                result.append(mapping[char])
            else:
                result.append(char)
        return ''.join(result), key
    
    def substitution_decode(self, text: str, key: str) -> str:
        """Decode using substitution cipher with provided key"""
        reverse_mapping = dict(zip(key, self.alphabet))
        result = []
        for char in text.lower():
            if char in reverse_mapping:
                result.append(reverse_mapping[char])
            else:
                result.append(char)
        return ''.join(result)
    
    def _generate_substitution_key(self) -> str:
        """Generate a random substitution key"""
        import random
        key = list(self.alphabet)
        random.shuffle(key)
        return ''.join(key)
    
    # ==================== ATBASH CIPHER ====================
    def atbash_encode(self, text: str) -> str:
        """Encode using Atbash cipher (reverse alphabet)"""
        result = []
        for char in text.lower():
            if char in self.alphabet:
                new_index = 25 - self.alphabet.index(char)
                result.append(self.alphabet[new_index])
            else:
                result.append(char)
        return ''.join(result)
    
    def atbash_decode(self, text: str) -> str:
        """Decode Atbash (same as encode - symmetric)"""
        return self.atbash_encode(text)
    
    # ==================== REVERSE CIPHER ====================
    def reverse_encode(self, text: str) -> str:
        """Encode by reversing the text"""
        return text[::-1]
    
    def reverse_decode(self, text: str) -> str:
        """Decode by reversing the text"""
        return text[::-1]
    
    # ==================== PIGPEN CIPHER ====================
    def pigpen_encode(self, text: str) -> str:
        """Encode using a simple Pigpen-like substitution"""
        pigpen_key = {
            'a': '⬜', 'b': '⬛', 'c': '✕', 'd': '✓',
            'e': '◆', 'f': '◇', 'g': '●', 'h': '○',
            'i': '⊞', 'j': '⊠', 'k': '♠', 'l': '♥',
            'm': '♣', 'n': '♦', 'o': '★', 'p': '☆',
            'q': '▲', 'r': '▼', 's': '◀', 't': '▶',
            'u': '█', 'v': '░', 'w': '▓', 'x': '▒',
            'y': '※', 'z': '§'
        }
        result = []
        for char in text.lower():
            result.append(pigpen_key.get(char, char))
        return ''.join(result)
    
    def pigpen_decode(self, text: str) -> str:
        """Decode Pigpen cipher"""
        reverse_pigpen = {
            '⬜': 'a', '⬛': 'b', '✕': 'c', '✓': 'd',
            '◆': 'e', '◇': 'f', '●': 'g', '○': 'h',
            '⊞': 'i', '⊠': 'j', '♠': 'k', '♥': 'l',
            '♣': 'm', '♦': 'n', '★': 'o', '☆': 'p',
            '▲': 'q', '▼': 'r', '◀': 's', '▶': 't',
            '█': 'u', '░': 'v', '▓': 'w', '▒': 'x',
            '※': 'y', '§': 'z'
        }
        result = []
        for char in text:
            result.append(reverse_pigpen.get(char, char))
        return ''.join(result)
    
    # ==================== VIGENERE CIPHER ====================
    def vigenere_encode(self, text: str, key: str) -> str:
        """Encode using Vigenere cipher"""
        key = key.lower()
        result = []
        key_index = 0
        
        for char in text.lower():
            if char in self.alphabet:
                shift = self.alphabet.index(key[key_index % len(key)])
                new_index = (self.alphabet.index(char) + shift) % 26
                result.append(self.alphabet[new_index])
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)
    
    def vigenere_decode(self, text: str, key: str) -> str:
        """Decode using Vigenere cipher"""
        key = key.lower()
        result = []
        key_index = 0
        
        for char in text.lower():
            if char in self.alphabet:
                shift = self.alphabet.index(key[key_index % len(key)])
                new_index = (self.alphabet.index(char) - shift) % 26
                result.append(self.alphabet[new_index])
                key_index += 1
            else:
                result.append(char)
        return ''.join(result)


def main():
    """Interactive cipher translator menu"""
    cipher = CipherTranslator()
    
    print("=" * 50)
    print("  ENCRYPTION/CIPHER TRANSLATOR")
    print("=" * 50)
    
    while True:
        print("\n📋 AVAILABLE CIPHERS:")
        print("1. Caesar Cipher (shift-based)")
        print("2. ROT13 Cipher")
        print("3. Substitution Cipher")
        print("4. Atbash Cipher (reverse alphabet)")
        print("5. Reverse Cipher")
        print("6. Pigpen Cipher (symbols)")
        print("7. Vigenere Cipher (keyword-based)")
        print("0. Exit")
        
        choice = input("\n👉 Select cipher (0-7): ").strip()
        
        if choice == '0':
            print("\n✅ Goodbye!")
            break
        
        elif choice == '1':
            text = input("📝 Enter text: ").strip()
            shift = input("🔑 Enter shift value (default 3): ").strip()
            shift = int(shift) if shift.isdigit() else 3
            action = input("🔄 Encode or Decode? (e/d): ").strip().lower()
            
            if action == 'e':
                result = cipher.caesar_encode(text, shift)
                print(f"✅ Encoded: {result}")
            else:
                result = cipher.caesar_decode(text, shift)
                print(f"✅ Decoded: {result}")
        
        elif choice == '2':
            text = input("📝 Enter text: ").strip()
            action = input("🔄 Encode or Decode? (e/d): ").strip().lower()
            
            if action == 'e':
                result = cipher.rot13_encode(text)
                print(f"✅ Encoded: {result}")
            else:
                result = cipher.rot13_decode(text)
                print(f"✅ Decoded: {result}")
        
        elif choice == '3':
            text = input("📝 Enter text: ").strip()
            action = input("🔄 Encode or Decode? (e/d): ").strip().lower()
            
            if action == 'e':
                key = input("🔑 Enter substitution key (press Enter for random): ").strip()
                result, used_key = cipher.substitution_encode(text, key if key else None)
                print(f"✅ Encoded: {result}")
                print(f"🔑 Key: {used_key}")
            else:
                key = input("🔑 Enter substitution key: ").strip()
                result = cipher.substitution_decode(text, key)
                print(f"✅ Decoded: {result}")
        
        elif choice == '4':
            text = input("📝 Enter text: ").strip()
            result = cipher.atbash_encode(text)
            print(f"✅ Result: {result}")
        
        elif choice == '5':
            text = input("📝 Enter text: ").strip()
            result = cipher.reverse_encode(text)
            print(f"✅ Result: {result}")
        
        elif choice == '6':
            text = input("📝 Enter text (a-z only): ").strip()
            action = input("🔄 Encode or Decode? (e/d): ").strip().lower()
            
            if action == 'e':
                result = cipher.pigpen_encode(text)
                print(f"✅ Encoded: {result}")
            else:
                result = cipher.pigpen_decode(text)
                print(f"✅ Decoded: {result}")
        
        elif choice == '7':
            text = input("📝 Enter text: ").strip()
            key = input("🔑 Enter keyword (no spaces): ").strip()
            action = input("🔄 Encode or Decode? (e/d): ").strip().lower()
            
            if action == 'e':
                result = cipher.vigenere_encode(text, key)
                print(f"✅ Encoded: {result}")
            else:
                result = cipher.vigenere_decode(text, key)
                print(f"✅ Decoded: {result}")
        
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
