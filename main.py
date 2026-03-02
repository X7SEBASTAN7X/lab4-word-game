def fib_list_recursive(n, seq=None):
	"""Return a list of the first `n` Fibonacci numbers, built recursively by
	appending each next number to `seq`.
	"""
	if n <= 0:
		return []
	if seq is None:
		seq = []
	if not seq:
		seq.append(0)
	if len(seq) >= n:
		return seq
	if len(seq) == 1:
		seq.append(1)
		return fib_list_recursive(n, seq)
	seq.append(seq[-1] + seq[-2])
	return fib_list_recursive(n, seq)


def fib_forget(n):
	"""Return the nth Fibonacci number (0-indexed) using naive recursion.
	This implementation does not remember previously computed values.
	"""
	if n < 0:
		raise ValueError("n must be non-negative")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_forget(n - 1) + fib_forget(n - 2)


if __name__ == "__main__":
	# Demo: first 10 Fibonacci numbers built by appending to a list
	print(fib_list_recursive(10))

	# Demo: compute each Fibonacci number separately (naive, forgetful)
	print([fib_forget(i) for i in range(10)])