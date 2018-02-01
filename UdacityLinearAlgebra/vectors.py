# This python file creates classes and methods to perform operations on vectors
import math


class Vectors:
    def __init__(self, coordinates):
        """
        Initializing a vector with coordinates
        :param coordinates: represent the coordinates of the vector
        """
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError("The coordinates must be non empty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return "Vector : {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    @staticmethod
    def add_vectors(*all_vectors):
        """
        Function to perform addition of vectors
        :param all_vectors: are all the vectors that have to be added up
        :return: a vector after performing the numerical addition
        """
        new_vector_dimension = all_vectors[0].dimension
        new_vector = [0] * new_vector_dimension

        # Performing tuple addition
        for vector in all_vectors:
            new_vector = [x + y for x, y in zip(list(vector.coordinates), new_vector)]

        return Vectors(new_vector)

    @staticmethod
    def subtract_vectors(*all_vectors):
        """
        Function to perform addition of vectors
        :param all_vectors: are all the vectors that have to be added up
        :return: a vector after performing the numerical addition
        """
        sub_new_vector = list(all_vectors[0].coordinates)

        # Performing tuple addition
        for vector in all_vectors[1:]:
            sub_new_vector = [x - y for x, y in zip(sub_new_vector, list(vector.coordinates))]
        return Vectors(sub_new_vector)

    @staticmethod
    def scalar_multiply(input_vector, scalar):
        """
        Function to perform scalar multiplication
        :param scalar: the scalar value with which the vector has to be multiplied with
        :param input_vector: the input vector
        :return: a new vector after the input vector is multiplied with the scalar value
        """
        return Vectors(list(scalar * coordinate for coordinate in input_vector.coordinates))

    def vector_magnitude(self):
        """
        Function to compute a vector's magnitude
        :return: the magnitude of the vector
        """
        return math.sqrt(sum([dimension ** 2 for dimension in self.coordinates]))

    def normalized_vector(self):
        """
        Function to calculate and return a normalized vector for the given vector
        :return: a vector like this vector with unit magnitude and in the same direction
        """
        return self.scalar_multiply(self, 1 / self.vector_magnitude())

    def dot_product_two_vectors(self, input_vector):
        """
        Function that calculates the dot product between this vector and the input vector
        :param input_vector: is a vector
        :return: the dot product ( a number )
        """
        return sum([x * y for x, y in zip(self.coordinates, input_vector.coordinates)])

    def angle_between_two_vectors_radians(self, input_vector):
        """
        Function to calculate the angle between 2 vectors
        :param input_vector: a vector
        :return: the angle this vector and the input vector in radians
        """
        return math.acos(self.dot_product_two_vectors(input_vector) /
                         (self.vector_magnitude() * input_vector.vector_magnitude()))

    def angle_between_two_vectors_in_degrees(self, input_vector):
        """
        Function to calculate the angle between 2 vectors
        :param input_vector: a vector
        :return: the angle this vector and the input vector in degrees
        """
        return math.degrees(self.angle_between_two_vectors_radians(input_vector))

    def check_two_vectors_parallel(self, input_vector):
        """
        Function to check if this vector is parallel to the input vector
        :param input_vector: a Vector
        :return: true, iff the input vector is parallel to this vector
                 false, otherwise
        """
        scalar = input_vector.coordinates[0] / self.coordinates[0]

        for self_coord, input_coord in zip(self.coordinates[1:], input_vector.coordinates[1:]):
            if input_coord / self_coord == scalar:
                continue
            else:
                return False

        return True

    def check_two_vectors_orthogonal(self, input_vector, tolerance=1e-10):
        """
        Function to check if the given vector(input vector) is orthogonal with this vector
        :param tolerance: Check against a tolerance level to avoid wrong answers due to precision values
        :param input_vector: a Vector
        :return: true, iff the 2 vectors are orthogonal
                 false, otherwise
        """
        return abs(self.dot_product_two_vectors(input_vector)) < tolerance

    def projection_along_basis_vector(self, basis_vector):
        """
        This function calculates the projection of this vector along the given basis vector
        :param basis_vector: is the basis vector which is assumed to be emanating from the origin
        :return: a projection of this vector along the basis vector
        """

        # Note: that projection of this vector is same as v parallel
        # which is then equal to normalized basis vector multipled by magnitude of this vector

        normalized_basis_vector = Vectors.normalized_vector(basis_vector)
        weight = self.dot_product_two_vectors(normalized_basis_vector)
        return self.scalar_multiply(normalized_basis_vector, weight)

    def orthogonal_projection(self, basis_vector):
        """
        Function to calculate the component of this vector along the orthogonal component of basis vector
        :param basis_vector: is the basis vector which is assumed to be emanating from the origin
        :return: component of this vector along the orthogonal component of basis vector
        """
        return Vectors.subtract_vectors(self, self.projection_along_basis_vector(basis_vector))

    def decompose_vectors(self, basis_vector):
        """
        Function to decompose this vector into parallel and orthogonal vectors
        :param basis_vector: the given basis vector assumed to be emanating from the origin
        :return: 2 decomposed vectors
        """

        return self.projection_along_basis_vector(basis_vector), self.orthogonal_projection(basis_vector)

    def cross_product_of_two_vectors(self, input_vector):
        """
        Function to find the cross product of this vector with the input vector passed as parameter
        :param input_vector: a vector
        :return: a Vector after performing cross product
        """
        x1, y1, z1 = self.coordinates[0], self.coordinates[1], self.coordinates[2]
        x2, y2, z2 = input_vector.coordinates[0], input_vector.coordinates[1], input_vector.coordinates[2]
        cross_list = [y1 * z2 - y2 * z1, x2 * z1 - x1 * z2, x1 * y2 - x2 * y1]
        return Vectors(cross_list)

    def area_of_parallelogram(self, input_vector):
        """
        Function which returns the area of the parallelogram spanned by the 2 vectors
        :param input_vector: a vector
        :return: the area of the parallelogram
        """

        return self.vector_magnitude() * Vectors.vector_magnitude(input_vector) * \
               math.sin(self.angle_between_two_vectors_radians(input_vector))

    def area_of_traingle_spanned(self, input_vector):
        """
        Function which returns the area of the triangle spanned by the 2 vectors
        :param input_vector: a vector
        :return: the area of the triangle
        """

        return 0.5 * self.area_of_parallelogram(input_vector)


v1 = Vectors([8.218, -9.341])
v2 = Vectors([-1.129, 2.111])

v3 = Vectors([7.119, 8.215])
v4 = Vectors([-8.223, 0.878])

v5 = Vectors([1.671, -1.012, -0.318])
scalar_multiplier = 7.41

# print(Vectors.add_vectors(v1, v2))
# print(Vectors.subtract_vectors(v3, v4))
# print(Vectors.scalar_multiply(v5, scalar_multiplier))

v6 = Vectors([-0.221, 7.437])
v7 = Vectors([8.813, -1.331, -6.247])
# print(v6.vector_magnitude())
# print(v7.vector_magnitude())

v8 = Vectors([5.581, -2.136])
v9 = Vectors([1.996, 3.108, -4.554])

# print(v8.normalized_vector())
# print(v9.normalized_vector())

v10 = Vectors([7.887, 4.138])
v11 = Vectors([-8.802, 6.776])
# print(v10.dot_product_two_vectors(v11))

v12 = Vectors([-5.955, -4.904, -1.874])
v13 = Vectors([-4.496, -8.755, 7.103])
# print(v12.dot_product_two_vectors(v13))

v14 = Vectors([3.183, -7.627])
v15 = Vectors([-2.668, 5.319])
# print(v14.angle_between_two_vectors_radians(v15))

v16 = Vectors([7.35, 0.221, 5.188])
v17 = Vectors([2.751, 8.259, 3.985])
# print(v16.angle_between_two_vectors_in_degrees(v17))

v18 = Vectors([-7.579, -7.88])
v19 = Vectors([22.737, 23.64])
# print(v18.check_two_vectors_parallel(v19))
# print(v18.check_two_vectors_orthogonal(v19))

v20 = Vectors([-2.029, 9.97, 4.172])
v21 = Vectors([-9.231, -6.639, -7.245])
# print(v20.check_two_vectors_parallel(v21))
# print(v20.check_two_vectors_orthogonal(v21))

v22 = Vectors([-2.328, -7.284, -1.214])
v23 = Vectors([-1.821, 1.072, -2.94])
# print(v22.check_two_vectors_parallel(v23))
# print(v22.check_two_vectors_orthogonal(v23))


v24 = Vectors([3.039, 1.879])
b01 = Vectors([0.825, 2.036])
# print(v24.projection_along_basis_vector(b01))

v25 = Vectors([-9.88, -3.264, -8.159])
b02 = Vectors([-2.155, -9.353, -9.473])
# print(v25.orthogonal_projection(b02))

v26 = Vectors([3.009, -6.172, 3.692, -2.51])
b03 = Vectors([6.404, -9.144, 2.759, 8.718])
decomposed_vectors = v26.decompose_vectors(b03)
parallel_component = decomposed_vectors[0]
orthogonal_component = decomposed_vectors[1]

# print(parallel_component.coordinates)
# print(orthogonal_component.coordinates)

v27 = Vectors([8.462, 7.893, -8.187])
v28 = Vectors([6.984, -5.975, 4.778])
# print(v27.cross_product_of_two_vectors(v28))

v29 = Vectors([-8.987, -9.838, 5.031])
v30 = Vectors([-4.268, -1.861, -8.866])
# print(v29.area_of_parallelogram(v30))

v31 = Vectors([1.5, 9.547, 3.691])
v32 = Vectors([-6.007, 0.124, 5.772])
# print(v31.area_of_traingle_spanned(v32))


v33 = Vectors([5, 5, 5])
v34 = Vectors([20, 30, 40])

print(v33.orthogonal_projection(v34))