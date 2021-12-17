import math


class Polygon:
	def __init__(self, num_edges: int, cir_radius: float):
		# Validate the edges and radius
		self._num_edges = num_edges
		self._cir_radius = cir_radius
		self.num_vertices = num_edges
		self.interior_angle = ((self._num_edges - 2) * 180) / self._num_edges
		angle_rad = math.pi/self._num_edges
		self.edge_length = 2 * self._cir_radius * math.sin(angle_rad)
		self.apothem = self._cir_radius * math.cos(angle_rad)
		self.area = (self._num_edges * self.edge_length * self.apothem) / 2
		self.perimeter = self._num_edges * self.edge_length

	def __repr__(self):
		return f'Polygon with {self._num_edges} edges and circum-radius = {self._cir_radius}'

	def __eq__(self, other):
		# check type of other
		if not isinstance(other,Polygon):
			raise TypeError(f"Argument passed is of type:{type(other)}, required type: Polygon")
		if (other._num_edges == self._num_edges) and (other._cir_radius == self._cir_radius):
			return True
		else:
			return False

	def __gt__(self, other):
		# check type of other
		if not isinstance(other, Polygon):
			raise TypeError(f"Argument passed is of type:{type(other)}, required type: Polygon")
		if self._num_edges > other._num_edges:
			return True
		else:
			return False


