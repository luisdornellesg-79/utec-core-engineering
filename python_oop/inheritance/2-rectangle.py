#!/usr/bin/env python3
"""Módulo que define la clase Rectangle basada en BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """Inicializa un rectángulo con ancho y alto validados.
        
        Args:
            width (int): El ancho del rectángulo.
            height (int): El alto del rectángulo.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación informal del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"
