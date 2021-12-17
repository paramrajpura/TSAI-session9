from Objective1 import Polygon


class Polygonseq:
    def __init__(self, max_num_edges, cir_rad):
        self._max_num_edges = max_num_edges
        self._min_num_edges = 3
        self._cir_radius = cir_rad
        self.max_eff_polygon = Polygon(num_edges=max_num_edges, cir_radius=cir_rad)

    def __getitem__(self, item):
        if isinstance(item, int):
            # single item requested
            if item < 0:
                item = self._max_num_edges - self._min_num_edges + 1 + item
            if item < 0 or item > self._max_num_edges - 1:
                raise IndexError
            return self._get_polygon(num_edges=self._min_num_edges + item)
        else:
            # handling for slice
            print(f'requesting [{item.start}:{item.stop}:{item.step}]')
            idx = item.indices(self._max_num_edges - self._min_num_edges + 1)
            rng = range(idx[0] + self._min_num_edges, idx[1] + self._min_num_edges, idx[2])
            return [self._get_polygon(num_edges=n) for n in rng]

    def _get_polygon(self, num_edges):
        return Polygon(num_edges, self._cir_radius)

    def __len__(self):
        return self._max_num_edges - self._min_num_edges + 1

    def __repr__(self):
        return f'Polygon sequence with num_edges = {[i for i in range(self._min_num_edges,self._max_num_edges+1)]} and circum-radius = {self._cir_radius}'
