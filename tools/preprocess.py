from utils import getBoundary

def preprocess(density=0.1, output="./data/points_train/points.npy"):
    '''
    parameter:
        density: how much voxel you want remove during the training, 1.0 means no remove, which is the same as the inference 

    Store the preprocess data in the ./data/points_train/points.npy
    '''
    dir_img = "./data/images/"
    dir_mask = "./data/labels"
    dir_out = output
    

    getBoundary()

def get_args():
    parser = argparse.ArgumentParser(description='Pre-process to prepare the dataset for the pointrender to train',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--point-density', metavar='D', type=float, nargs='?', default=0.1,
                        help='Point Density', dest='pointdensity')
    parser.add_argument('-o', '--output', metavar='O', type=str, nargs='?', default="./data/points_train/points.npy",
                        help='Output', dest='o')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    
    net.to(device=device)

    try:
        train_net(net=net,
                  epochs=args.epochs,
                  batch_size=args.batchsize,
                  lr=args.lr,
                  device=device,
                  val_percent=args.val / 100)
    except KeyboardInterrupt:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
