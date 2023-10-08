def selection_sort(vector: list[int]) -> list[int]:
    vector_ = vector.copy()
    for i in range(len(vector) - 1):
        min = vector_[i]
        min_index = i
        for j in range(i + 1, len(vector)):
            if vector_[j] < min:
                min = vector_[j]
                min_index = j
        old_i_value = vector_[i]
        vector_[i] = min
        if min_index != i:
            vector_[min_index] = old_i_value
    return vector_
