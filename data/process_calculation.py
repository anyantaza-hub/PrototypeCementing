def calculate_pressure(md, flow):
    return md * flow * 12.3

def calculate_laminar(flow, dia, vis):
    return (4 * flow) / (3.14 * dia**2 * vis)
